#
# PySNMP MIB module CISCO-FC-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FC-MULTICAST-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
DomainIdOrZero, = mibBuilder.importSymbols("CISCO-ST-TC", "DomainIdOrZero")
vsanIndex, = mibBuilder.importSymbols("CISCO-VSAN-MIB", "vsanIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
ciscoFcMulticastMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 435))
ciscoFcMulticastMIB.setRevisions(('2004-10-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFcMulticastMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoFcMulticastMIB.setLastUpdated('200410070000Z')
if mibBuilder.loadTexts: ciscoFcMulticastMIB.setOrganization('Cisco Systems Inc. ')
if mibBuilder.loadTexts: ciscoFcMulticastMIB.setContactInfo('     Cisco Systems\n                      Customer Service\n                Postal: 170 W Tasman Drive\n                      San Jose, CA  95134\n                      USA\n                Tel: +1 800 553 -NETS\n                E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoFcMulticastMIB.setDescription('MIB module for monitoring and configuring \n                Fibre Channel Multicast feature.')
ciscoFcMulticastNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 0))
ciscoFcMulticastMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 1))
ciscoFcMulticaseConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 2))
cfmConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1))
class CfmMulticastRootMode(TextualConvention, Integer32):
    reference = 'Refer to FC-SW-2 REV 5.4 for information on principal \n              switch and lowest domain id switch.'
    description = 'The multicast Root Mode.\n                principalSwitch       - principal switch is used as the\n                                        root for multicast tree \n                                        computation.\n                lowestDomainIdSwitch  - lowest domainId switch is used \n                                        as the root for mulitcast tree \n                                        computation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("principalSwitch", 1), ("lowestDomainSwitch", 2))

cfmMulticastRootTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1), )
if mibBuilder.loadTexts: cfmMulticastRootTable.setReference('For information FC multicast/root, refer to Fibre Channel \n           Switch Fabric-2  (FC-SW-2 REV 5.4) and Fibre Channel Switch \n           Fabric-3  (FC-SW-3 REV 6.6).')
if mibBuilder.loadTexts: cfmMulticastRootTable.setStatus('current')
if mibBuilder.loadTexts: cfmMulticastRootTable.setDescription("This table allows the users to configure and monitor the\n           FC Multicast parameters on all the VSANs configured on the \n           local switch.\n\n           An entry is automatically created in this table if there\n           is an entry in the fspfTable (defined in CISCO-FSPF-MIB) and\n           fspfOperStatus (defined in CISCO-FSPF-MIB) for that\n           entry is 'up'.\n \n           An entry is automatically deleted from this table if\n           either :\n            a) the fspfOperStatus in the fspfTable entry for the \n               corresponding VSAN changes to 'down'.\n                                 or\n            b) the fspfTable entry for the corresponding VSAN is\n               deleted.\n\n           Entries in this table can be created via \n           cfmMulticastRootRowStatus only as the means to specify \n           non-default parameter values for a VSAN either because the\n           VSAN is suspended or fspfOperStatus (defined in \n           CISCO-FSPF-MIB) for that VSAN is 'down' (VSAN state is \n           indicated by object vsanOperState which is defined in \n           CISCO-VSAN-MIB).\n\n           So an entry in this table exists when one or both of these\n           conditions holds:\n           - one or more configuration parameters have non-default\n             values for a VSAN which is either suspended or the \n             fspfOperStatus for that VSAN is down.  \n           - the fspfOperStatus for VSAN is 'up'.\n\n           This has a number of consequences:\n           - an entry exists for a suspended VSAN whenever that VSAN \n             has non-default parameters.\n           - an entry cannot be created (via cfmMulticastRootRowStatus) \n             for a VSAN with default parameters; instead, the agent\n             creates/deletes an entry for a VSAN with default\n             parameters according to whether the fspfOperStatus is 'up' \n             or 'down'.\n           - an entry can not be created via cfmMulticastRootRowStatus \n             unless non-default parameter values are (simultaneously) \n             configured for a VSAN whose fspfOperStatus is 'down'.\n           - deleting an entry via cfmMulticastRootRowStatus when either\n             the VSAN is suspended and configured with non-default \n             values or the VSAN is active, is equivalent to resetting\n             its parameters to their default values.\n             If an entry is configured with default-values and the \n             VSAN is in suspended state, then the entry would be \n             deleted.")
cfmMulticastRootEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: cfmMulticastRootEntry.setStatus('current')
if mibBuilder.loadTexts: cfmMulticastRootEntry.setDescription('This entry contains the multicase parameters on this VSAN.')
cfmMulticastRootConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 1), CfmMulticastRootMode().clone('principalSwitch')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMulticastRootConfigMode.setStatus('current')
if mibBuilder.loadTexts: cfmMulticastRootConfigMode.setDescription('The configured multicast root mode on this VSAN.')
cfmMulticastRootOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 2), CfmMulticastRootMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMulticastRootOperMode.setStatus('current')
if mibBuilder.loadTexts: cfmMulticastRootOperMode.setDescription('The operational multicast root mode on this VSAN.')
cfmMulticastRootDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 3), DomainIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMulticastRootDomainId.setStatus('current')
if mibBuilder.loadTexts: cfmMulticastRootDomainId.setDescription('The domainID of the multicast root on this VSAN.')
cfmMulticastRootRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMulticastRootRowStatus.setStatus('current')
if mibBuilder.loadTexts: cfmMulticastRootRowStatus.setDescription('The status of conceptual row on this VSAN.\n\n           This object can be used to create an entry only if\n           either the corresponding VSAN is suspended or the\n           fspfOperStatus is down. If the VSAN is either \n           not-existent or fspfOperStatus is up, the create will fail.')
ciscoFcMulticastMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 1))
ciscoFcMulticastMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 2))
ciscoFcMulticastMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 1, 1)).setObjects(("CISCO-FC-MULTICAST-MIB", "cfmConfigurationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcMulticastMIBCompliance = ciscoFcMulticastMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoFcMulticastMIBCompliance.setDescription('The compliance statement for entities which implement the \n           CISCO-FC-MULTICAST-MIB.')
cfmConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 2, 1)).setObjects(("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootConfigMode"), ("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootOperMode"), ("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootDomainId"), ("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmConfigurationGroup = cfmConfigurationGroup.setStatus('current')
if mibBuilder.loadTexts: cfmConfigurationGroup.setDescription('A collection of objects for FC multicast \n           configuration.')
mibBuilder.exportSymbols("CISCO-FC-MULTICAST-MIB", CfmMulticastRootMode=CfmMulticastRootMode, cfmMulticastRootRowStatus=cfmMulticastRootRowStatus, ciscoFcMulticastMIBGroups=ciscoFcMulticastMIBGroups, ciscoFcMulticastNotifications=ciscoFcMulticastNotifications, PYSNMP_MODULE_ID=ciscoFcMulticastMIB, cfmConfiguration=cfmConfiguration, cfmMulticastRootConfigMode=cfmMulticastRootConfigMode, ciscoFcMulticastMIBCompliance=ciscoFcMulticastMIBCompliance, ciscoFcMulticastMIB=ciscoFcMulticastMIB, cfmMulticastRootOperMode=cfmMulticastRootOperMode, cfmConfigurationGroup=cfmConfigurationGroup, ciscoFcMulticastMIBCompliances=ciscoFcMulticastMIBCompliances, cfmMulticastRootDomainId=cfmMulticastRootDomainId, ciscoFcMulticastMIBObjects=ciscoFcMulticastMIBObjects, cfmMulticastRootEntry=cfmMulticastRootEntry, ciscoFcMulticaseConformance=ciscoFcMulticaseConformance, cfmMulticastRootTable=cfmMulticastRootTable)
