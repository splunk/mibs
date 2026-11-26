#
# PySNMP MIB module DLINKSW-TRAFFIC-SEGMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-TRAFFIC-SEGMENT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:25 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Bits, Counter64, TimeTicks, NotificationType, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, IpAddress, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Bits", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "IpAddress", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DLINKSW-TRAFFIC-SEGMENT-MIB", PYSNMP_MODULE_ID=dlinkSwTrafficSegMIB, dTrafficSegMIBCompliance=dTrafficSegMIBCompliance, dTrafficSegForwardPorts=dTrafficSegForwardPorts, dTrafficSegMIBCompliances=dTrafficSegMIBCompliances, dTrafficSegForwardDomainTable=dTrafficSegForwardDomainTable, dlinkSwTrafficSegMIB=dlinkSwTrafficSegMIB, dTrafficSegMIBGroups=dTrafficSegMIBGroups, dTrafficSegNotifications=dTrafficSegNotifications, dTrafficSegIfCfgGroup=dTrafficSegIfCfgGroup, dTrafficSegObjects=dTrafficSegObjects, dTrafficSegForwardDomainEntry=dTrafficSegForwardDomainEntry, dTrafficSegConformance=dTrafficSegConformance)
