#
# PySNMP MIB module DLINKSW-TRAFFIC-SEGMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-TRAFFIC-SEGMENT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Counter64, IpAddress, ModuleIdentity, Gauge32, Unsigned32, Bits, iso, ObjectIdentity, Integer32, NotificationType, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "IpAddress", "ModuleIdentity", "Gauge32", "Unsigned32", "Bits", "iso", "ObjectIdentity", "Integer32", "NotificationType", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlinkSwTrafficSegMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 26))
dlinkSwTrafficSegMIB.setRevisions(('2013-03-01 00:00',))
if mibBuilder.loadTexts: dlinkSwTrafficSegMIB.setLastUpdated('201303010000Z')
if mibBuilder.loadTexts: dlinkSwTrafficSegMIB.setOrganization('D-Link Corp.')
dTrafficSegNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 26, 0))
dTrafficSegObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 26, 1))
dTrafficSegConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 26, 2))
dTrafficSegForwardDomainTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 26, 1, 1), )
if mibBuilder.loadTexts: dTrafficSegForwardDomainTable.setStatus('current')
dTrafficSegForwardDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 26, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dTrafficSegForwardDomainEntry.setStatus('current')
dTrafficSegForwardPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 26, 1, 1, 1, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dTrafficSegForwardPorts.setStatus('current')
dTrafficSegMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 26, 2, 1))
dTrafficSegMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 26, 2, 2))
dTrafficSegMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 26, 2, 1, 1)).setObjects(("DLINKSW-TRAFFIC-SEGMENT-MIB", "dTrafficSegIfCfgGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dTrafficSegMIBCompliance = dTrafficSegMIBCompliance.setStatus('current')
dTrafficSegIfCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 26, 2, 2, 1)).setObjects(("DLINKSW-TRAFFIC-SEGMENT-MIB", "dTrafficSegForwardPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dTrafficSegIfCfgGroup = dTrafficSegIfCfgGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-TRAFFIC-SEGMENT-MIB", dTrafficSegMIBGroups=dTrafficSegMIBGroups, dTrafficSegNotifications=dTrafficSegNotifications, PYSNMP_MODULE_ID=dlinkSwTrafficSegMIB, dTrafficSegIfCfgGroup=dTrafficSegIfCfgGroup, dTrafficSegObjects=dTrafficSegObjects, dTrafficSegForwardPorts=dTrafficSegForwardPorts, dlinkSwTrafficSegMIB=dlinkSwTrafficSegMIB, dTrafficSegForwardDomainTable=dTrafficSegForwardDomainTable, dTrafficSegForwardDomainEntry=dTrafficSegForwardDomainEntry, dTrafficSegMIBCompliances=dTrafficSegMIBCompliances, dTrafficSegMIBCompliance=dTrafficSegMIBCompliance, dTrafficSegConformance=dTrafficSegConformance)
