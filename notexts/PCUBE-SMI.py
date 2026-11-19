#
# PySNMP MIB module PCUBE-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/PCUBE-SMI
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, NotificationType, enterprises, Counter64, Gauge32, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "NotificationType", "enterprises", "Counter64", "Gauge32", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pcube = ModuleIdentity((1, 3, 6, 1, 4, 1, 5655))
pcube.setRevisions(('2002-01-14 20:00',))
if mibBuilder.loadTexts: pcube.setLastUpdated('200201142000Z')
if mibBuilder.loadTexts: pcube.setOrganization('Cisco Systems, Inc.')
pcubeProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 5655, 1))
if mibBuilder.loadTexts: pcubeProducts.setStatus('current')
pcubeModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 5655, 2))
if mibBuilder.loadTexts: pcubeModules.setStatus('current')
pcubeMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 5655, 3))
if mibBuilder.loadTexts: pcubeMgmt.setStatus('current')
pcubeWorkgroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5655, 4))
if mibBuilder.loadTexts: pcubeWorkgroup.setStatus('current')
mibBuilder.exportSymbols("PCUBE-SMI", pcubeModules=pcubeModules, pcubeProducts=pcubeProducts, pcubeMgmt=pcubeMgmt, PYSNMP_MODULE_ID=pcube, pcube=pcube, pcubeWorkgroup=pcubeWorkgroup)
