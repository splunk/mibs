#
# PySNMP MIB module DLINKSW-TRAFFIC-SEGMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-TRAFFIC-SEGMENT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:48 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, ObjectIdentity, ModuleIdentity, Bits, IpAddress, iso, NotificationType, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Bits", "IpAddress", "iso", "NotificationType", "MibIdentifier", "Unsigned32")
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
mibBuilder.exportSymbols("DLINKSW-TRAFFIC-SEGMENT-MIB", dTrafficSegMIBCompliances=dTrafficSegMIBCompliances, dTrafficSegForwardPorts=dTrafficSegForwardPorts, dTrafficSegMIBGroups=dTrafficSegMIBGroups, dTrafficSegMIBCompliance=dTrafficSegMIBCompliance, dTrafficSegForwardDomainTable=dTrafficSegForwardDomainTable, dlinkSwTrafficSegMIB=dlinkSwTrafficSegMIB, dTrafficSegObjects=dTrafficSegObjects, dTrafficSegForwardDomainEntry=dTrafficSegForwardDomainEntry, dTrafficSegNotifications=dTrafficSegNotifications, dTrafficSegConformance=dTrafficSegConformance, PYSNMP_MODULE_ID=dlinkSwTrafficSegMIB, dTrafficSegIfCfgGroup=dTrafficSegIfCfgGroup)
