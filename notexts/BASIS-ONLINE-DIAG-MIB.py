#
# PySNMP MIB module BASIS-ONLINE-DIAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/BASIS-ONLINE-DIAG-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
axisDiagnostics, = mibBuilder.importSymbols("BASIS-MIB", "axisDiagnostics")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
basisOnlineDiagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 80))
basisOnlineDiagMIB.setRevisions(('2003-06-11 00:00',))
if mibBuilder.loadTexts: basisOnlineDiagMIB.setLastUpdated('200306110000Z')
if mibBuilder.loadTexts: basisOnlineDiagMIB.setOrganization('Cisco Systems, Inc.')
onlineDiagnostics = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 6, 3))
diagType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("post", 1), ("onlinediag", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diagType.setStatus('current')
diagResult = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("passed", 1), ("failed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diagResult.setStatus('current')
diagTestId = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diagTestId.setStatus('current')
boDiagMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 80, 2))
boDiagMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 1))
boDiagMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 2))
boDiagCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 1, 1)).setObjects(("BASIS-ONLINE-DIAG-MIB", "boDiagGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    boDiagCompliance = boDiagCompliance.setStatus('current')
boDiagGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 2, 1)).setObjects(("BASIS-ONLINE-DIAG-MIB", "diagType"), ("BASIS-ONLINE-DIAG-MIB", "diagResult"), ("BASIS-ONLINE-DIAG-MIB", "diagTestId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    boDiagGroup = boDiagGroup.setStatus('current')
mibBuilder.exportSymbols("BASIS-ONLINE-DIAG-MIB", PYSNMP_MODULE_ID=basisOnlineDiagMIB, boDiagCompliance=boDiagCompliance, basisOnlineDiagMIB=basisOnlineDiagMIB, boDiagGroup=boDiagGroup, onlineDiagnostics=onlineDiagnostics, diagTestId=diagTestId, boDiagMIBConformance=boDiagMIBConformance, diagType=diagType, diagResult=diagResult, boDiagMIBGroups=boDiagMIBGroups, boDiagMIBCompliances=boDiagMIBCompliances)
