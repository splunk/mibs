#
# PySNMP MIB module CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
TimeInterval, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TextualConvention", "DisplayString")
ciscoDot11CsMgrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 3228))
ciscoDot11CsMgrMIB.setRevisions(('2003-11-02 00:00',))
if mibBuilder.loadTexts: ciscoDot11CsMgrMIB.setLastUpdated('200311020000Z')
if mibBuilder.loadTexts: ciscoDot11CsMgrMIB.setOrganization('Cisco Systems Inc.')
ciscoDot11CsMgrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1))
ciscoDot11CsMgrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 3228, 2))
ciscoDot11CsMgrClientConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1))
class Cdot11CsModuleIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

cDot11CsMgrClientTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1), )
if mibBuilder.loadTexts: cDot11CsMgrClientTable.setStatus('current')
cDot11CsMgrClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntModuleIndex"))
if mibBuilder.loadTexts: cDot11CsMgrClientEntry.setStatus('current')
cDot11CsMgrClntModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 1), Cdot11CsModuleIndex())
if mibBuilder.loadTexts: cDot11CsMgrClntModuleIndex.setStatus('current')
cDot11CsMgrClntAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CsMgrClntAddressType.setStatus('current')
cDot11CsMgrClntParentWdsAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CsMgrClntParentWdsAddr.setStatus('current')
cDot11CsMgrClntRootNodeAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CsMgrClntRootNodeAddr.setStatus('current')
cDot11CsMgrClntMnAuthenAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CsMgrClntMnAuthenAddr.setStatus('current')
cDot11CsMgrClntOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("infrastructure", 1), ("distributed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CsMgrClntOperMode.setStatus('current')
cDot11CsMgrClntRegistLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 7), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CsMgrClntRegistLifeTime.setStatus('current')
cDot11CsMgrClntStateTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CsMgrClntStateTransitions.setStatus('current')
ciscoDot11CsMgrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 3228, 2, 1))
ciscoDot11CsMgrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 3228, 2, 2))
ciscoDot11CsMgrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 3228, 2, 1, 1)).setObjects(("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "ciscoDot11CsMgrClientGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CsMgrMIBCompliance = ciscoDot11CsMgrMIBCompliance.setStatus('current')
ciscoDot11CsMgrClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 3228, 2, 2, 1)).setObjects(("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntAddressType"), ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntParentWdsAddr"), ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntRootNodeAddr"), ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntMnAuthenAddr"), ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntOperMode"), ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntRegistLifeTime"), ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntStateTransitions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CsMgrClientGroup = ciscoDot11CsMgrClientGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", PYSNMP_MODULE_ID=ciscoDot11CsMgrMIB, cDot11CsMgrClientEntry=cDot11CsMgrClientEntry, ciscoDot11CsMgrClientGroup=ciscoDot11CsMgrClientGroup, cDot11CsMgrClntParentWdsAddr=cDot11CsMgrClntParentWdsAddr, cDot11CsMgrClntAddressType=cDot11CsMgrClntAddressType, ciscoDot11CsMgrMIBGroups=ciscoDot11CsMgrMIBGroups, ciscoDot11CsMgrMIBConformance=ciscoDot11CsMgrMIBConformance, cDot11CsMgrClntModuleIndex=cDot11CsMgrClntModuleIndex, cDot11CsMgrClntStateTransitions=cDot11CsMgrClntStateTransitions, ciscoDot11CsMgrMIBCompliances=ciscoDot11CsMgrMIBCompliances, cDot11CsMgrClntRegistLifeTime=cDot11CsMgrClntRegistLifeTime, ciscoDot11CsMgrClientConfig=ciscoDot11CsMgrClientConfig, Cdot11CsModuleIndex=Cdot11CsModuleIndex, cDot11CsMgrClntMnAuthenAddr=cDot11CsMgrClntMnAuthenAddr, cDot11CsMgrClientTable=cDot11CsMgrClientTable, cDot11CsMgrClntRootNodeAddr=cDot11CsMgrClntRootNodeAddr, ciscoDot11CsMgrMIBCompliance=ciscoDot11CsMgrMIBCompliance, ciscoDot11CsMgrMIB=ciscoDot11CsMgrMIB, cDot11CsMgrClntOperMode=cDot11CsMgrClntOperMode, ciscoDot11CsMgrMIBObjects=ciscoDot11CsMgrMIBObjects)
