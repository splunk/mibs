#
# PySNMP MIB module CLOUDGENIX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cloudgenix/CLOUDGENIX-SMI
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:35 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, MibIdentifier, Counter32, ModuleIdentity, iso, IpAddress, Unsigned32, Bits, TimeTicks, ObjectIdentity, enterprises, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "Counter32", "ModuleIdentity", "iso", "IpAddress", "Unsigned32", "Bits", "TimeTicks", "ObjectIdentity", "enterprises", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cloudgenix = ModuleIdentity((1, 3, 6, 1, 4, 1, 50114))
cloudgenix.setRevisions(('2017-06-19 18:00',))
if mibBuilder.loadTexts: cloudgenix.setLastUpdated('202202241935Z')
if mibBuilder.loadTexts: cloudgenix.setOrganization('Palo Alto Networks, Inc.')
class CgxDegreesC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-3'

class CgxVolts(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-3'

cgxObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 1))
cgxConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 2))
cgxCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 2, 1))
cloudgenixCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 50114, 2, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cloudgenixCompliance = cloudgenixCompliance.setStatus('current')
cgxGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 2, 2))
cgxMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 50114, 10))
if mibBuilder.loadTexts: cgxMgmt.setStatus('current')
cgxProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 50114, 11))
if mibBuilder.loadTexts: cgxProducts.setStatus('current')
mibBuilder.exportSymbols("CLOUDGENIX-SMI", cgxCompliances=cgxCompliances, cloudgenixCompliance=cloudgenixCompliance, cloudgenix=cloudgenix, CgxVolts=CgxVolts, CgxDegreesC=CgxDegreesC, cgxMgmt=cgxMgmt, cgxGroups=cgxGroups, cgxProducts=cgxProducts, cgxObjects=cgxObjects, PYSNMP_MODULE_ID=cloudgenix, cgxConformance=cgxConformance)
