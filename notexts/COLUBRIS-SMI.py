#
# PySNMP MIB module COLUBRIS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-SMI
# Produced by pysmi-1.1.12 at Thu Nov 19 14:37:01 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, ObjectIdentity, Bits, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, MibIdentifier, Unsigned32, ModuleIdentity, Integer32, Gauge32, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ObjectIdentity", "Bits", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Integer32", "Gauge32", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
colubris = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744))
if mibBuilder.loadTexts: colubris.setLastUpdated('200402100000Z')
if mibBuilder.loadTexts: colubris.setOrganization('Colubris Networks, Inc.')
colubrisProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 1))
if mibBuilder.loadTexts: colubrisProducts.setStatus('current')
colubrisMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 2))
if mibBuilder.loadTexts: colubrisMgmt.setStatus('deprecated')
colubrisExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 3))
if mibBuilder.loadTexts: colubrisExperiment.setStatus('current')
colubrisModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 4))
if mibBuilder.loadTexts: colubrisModules.setStatus('current')
colubrisMgmtV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 5))
if mibBuilder.loadTexts: colubrisMgmtV2.setStatus('current')
extensions = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 6))
if mibBuilder.loadTexts: extensions.setStatus('current')
variation = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 7))
if mibBuilder.loadTexts: variation.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-SMI", colubrisExperiment=colubrisExperiment, extensions=extensions, variation=variation, PYSNMP_MODULE_ID=colubris, colubrisMgmtV2=colubrisMgmtV2, colubrisProducts=colubrisProducts, colubris=colubris, colubrisMgmt=colubrisMgmt, colubrisModules=colubrisModules)
