#
# PySNMP MIB module DLINKSW-TRAFFIC-SEGMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-TRAFFIC-SEGMENT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:45 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, ModuleIdentity, TimeTicks, Gauge32, iso, NotificationType, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, MibIdentifier, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "TimeTicks", "Gauge32", "iso", "NotificationType", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlinkSwTrafficSegMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 26))
dlinkSwTrafficSegMIB.setRevisions(('2013-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlinkSwTrafficSegMIB.setRevisionsDescriptions(('This is the first version of the MIB file.',))
if mibBuilder.loadTexts: dlinkSwTrafficSegMIB.setLastUpdated('201303010000Z')
if mibBuilder.loadTexts: dlinkSwTrafficSegMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: dlinkSwTrafficSegMIB.setContactInfo('        D-Link Corporation\n\n             Postal: No. 289, Sinhu 3rd Rd., Neihu District,\n                     Taipei City 114, Taiwan, R.O.C\n             Tel:     +886-2-66000123\n             E-mail: tsd@dlink.com.tw\n            ')
if mibBuilder.loadTexts: dlinkSwTrafficSegMIB.setDescription('This MIB module defines objects for Traffic Segmentation.')
dTrafficSegNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 26, 0))
dTrafficSegObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 26, 1))
dTrafficSegConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 26, 2))
dTrafficSegForwardDomainTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 26, 1, 1), )
if mibBuilder.loadTexts: dTrafficSegForwardDomainTable.setStatus('current')
if mibBuilder.loadTexts: dTrafficSegForwardDomainTable.setDescription('A list of specification of forwarding domains for Traffic Segmentation.')
dTrafficSegForwardDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 26, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dTrafficSegForwardDomainEntry.setStatus('current')
if mibBuilder.loadTexts: dTrafficSegForwardDomainEntry.setDescription('An entry indicates the setting of forwarding domain on an interface.')
dTrafficSegForwardPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 26, 1, 1, 1, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dTrafficSegForwardPorts.setStatus('current')
if mibBuilder.loadTexts: dTrafficSegForwardPorts.setDescription('This object indicates the forward domain (a set of ports) on the\n            interface.')
dTrafficSegMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 26, 2, 1))
dTrafficSegMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 26, 2, 2))
dTrafficSegMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 26, 2, 1, 1)).setObjects(("DLINKSW-TRAFFIC-SEGMENT-MIB", "dTrafficSegIfCfgGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dTrafficSegMIBCompliance = dTrafficSegMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: dTrafficSegMIBCompliance.setDescription('The compliance statement for entities which implement the \n            DLINKSW-TRAFFIC-SEGMENT-MIB.')
dTrafficSegIfCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 26, 2, 2, 1)).setObjects(("DLINKSW-TRAFFIC-SEGMENT-MIB", "dTrafficSegForwardPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dTrafficSegIfCfgGroup = dTrafficSegIfCfgGroup.setStatus('current')
if mibBuilder.loadTexts: dTrafficSegIfCfgGroup.setDescription('A collection of objects providing management of the Traffic\n            Segmentation feature.')
mibBuilder.exportSymbols("DLINKSW-TRAFFIC-SEGMENT-MIB", dTrafficSegForwardDomainEntry=dTrafficSegForwardDomainEntry, dTrafficSegMIBCompliance=dTrafficSegMIBCompliance, dTrafficSegForwardDomainTable=dTrafficSegForwardDomainTable, dTrafficSegIfCfgGroup=dTrafficSegIfCfgGroup, dTrafficSegMIBCompliances=dTrafficSegMIBCompliances, dTrafficSegMIBGroups=dTrafficSegMIBGroups, PYSNMP_MODULE_ID=dlinkSwTrafficSegMIB, dTrafficSegForwardPorts=dTrafficSegForwardPorts, dlinkSwTrafficSegMIB=dlinkSwTrafficSegMIB, dTrafficSegNotifications=dTrafficSegNotifications, dTrafficSegObjects=dTrafficSegObjects, dTrafficSegConformance=dTrafficSegConformance)
